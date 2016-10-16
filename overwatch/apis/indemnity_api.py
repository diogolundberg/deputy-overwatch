from flask import Blueprint, jsonify, request
from overwatch.models import Indemnity, Deputy
from webargs import fields
from webargs.flaskparser import use_args
from sqlalchemy import desc, func, extract
from decimal import Decimal
from inflection import singularize


blueprint = Blueprint('indemnity_api', __name__, url_prefix='/api/indemnities')


@blueprint.route('/')
def list():
    indemnities = [dict(i) for i in Indemnity.query.all()]
    return jsonify(indemnities=indemnities), 200


@blueprint.route('/categories/')
@use_args({
    'top': fields.Integer(required=False)
})
def categories(args):
    top = args.get('top')

    query = Indemnity.query.join(Deputy).with_entities(
        Indemnity.category,
        func.sum(Indemnity.value).label("total_budget"),
    ).group_by(
        Indemnity.category_id,
    ).order_by(
        desc(func.sum(Indemnity.value))
    )

    return jsonify(categories=group_by_parent_serialize(query, 'categories', top)), 200


@blueprint.route('/categories/deputies/')
@use_args({
    'top': fields.Integer(required=False)
})
def categories_deputies(args):
    top = args.get('top')

    query = Indemnity.query.join(Deputy).with_entities(
        Indemnity.category,
        Deputy.name,
        Deputy.party,
        func.sum(Indemnity.value).label("total_budget"),
    ).group_by(
        Indemnity.category_id,
        Indemnity.deputy_id,
    ).order_by(
        desc(func.sum(Indemnity.value))
    )

    return jsonify(categories=group_by_parent_parent_serialize(query, 'category', 'deputies', top))


def group_by_parent_serialize(query, parent, top=None):
    serializable = {}
    child_columns = [c['name'] for c in query.column_descriptions if c['name'] != singularize(parent)]

    for result in query.all():
        row = [c for c in result]
        parent_name = row.pop(0)
        child = {}

        for value in row:
            child_property = child_columns[row.index(value)]
            child[child_property] = float(value) if isinstance(value, Decimal) else value

        if not top or len(serializable) < top:
            serializable[parent_name] = child

    return serializable


def group_by_parent_parent_serialize(query, grand_parent, parent, top=None):
    serializable = {}
    child_columns = [c['name'] for c in query.column_descriptions if c['name'] != singularize(grand_parent)]

    for result in query.all():
        row = [c for c in result]
        grand_parent_name = row.pop(0)
        child = {}

        for value in row:
            child_property = child_columns[row.index(value)]
            child[child_property] = float(value) if isinstance(value, Decimal) else value

        if grand_parent_name in serializable:
            if not top or len(serializable[grand_parent_name][parent]) < top:
                serializable[grand_parent_name][parent].append(child)
        else:
            serializable[grand_parent_name] = {}
            serializable[grand_parent_name][parent] = [child]

    return serializable
