from flask_script import Command
from overwatch.scripts import deputy_loader, budget_date_loader
from overwatch.models import Deputy, BudgetDate


class Scrape(Command):
    "Scrape and load the ALMG data into the database"

    def run(self):
        deputy_loader.update_deputies()
        self.deputies = Deputy.query.all()
        budget_date_loader.update_budget_dates(self.deputies)
        print("Data scrapped!")