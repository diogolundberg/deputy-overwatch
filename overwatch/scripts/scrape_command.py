import time
from flask_script import Command
from overwatch.scripts import deputy_loader, budget_date_loader, indemnity_loader
from overwatch.models import Deputy, BudgetDate


class Scrape(Command):

    "Scrape and load the ALMG data into the database (will take about 6 minutes)"

    def run(self):
        start_time = time.time()
        deputy_loader.update_deputies()
        self.deputies = Deputy.query.all()
        budget_date_loader.update_budget_dates(self.deputies)
        self.budget_dates = BudgetDate.query.all()
        indemnity_loader.update_indemnities(self.budget_dates)

        minutes, seconds = divmod(time.time() - start_time, 60)
        time_elapsed = '{:0>2} minutes and {:0>2} seconds'.format(
            int(minutes), int(seconds))

        print("Data scrapped! (%s)" % time_elapsed)
