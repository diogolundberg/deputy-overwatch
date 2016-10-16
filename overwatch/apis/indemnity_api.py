from flask import Blueprint, jsonify, request
from overwatch.models import Indemnity, Deputy
from webargs import fields
from webargs.flaskparser import use_args
from sqlalchemy import desc, func
from decimal import Decimal


blueprint = Blueprint('indemnity_api', __name__, url_prefix='/api/indemnities')



@blueprint.route('/')
def list():
    indemnities = [dict(i) for i in Indemnity.query.all()]
    return jsonify(indemnities = indemnities), 200


args = {
    'top': fields.Integer(required=False)
}

@blueprint.route('/categories/deputies/')
@use_args(args)
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

    return jsonify(categories = parent_child_serialize(query, 'category', 'deputies', top))


def parent_child_serialize(query, parent_column, child_name, top=None):
    serializable = {}
    columns = [c['name'] for c in query.column_descriptions if c['name'] != parent_column]

    for result in query.all():
        row = [c for c in result]
        parent_name = row.pop(0)
        child = {}

        for item in row:
            child_column = columns[row.index(item)]
            child[child_column] = float(item) if isinstance(item, Decimal) else item

        if parent_name in serializable:
            if not top or len(serializable[parent_name]) < top:
                serializable[parent_name][child_name].append(child)
        else:
            serializable[parent_name] = {}
            serializable[parent_name][child_name] = [child]

    return serializable