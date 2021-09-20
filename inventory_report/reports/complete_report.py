from typing import Counter, List
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(inventory: List) -> str:
        report = SimpleReport.generate(inventory)
        report += CompleteReport.calculate_products_by_company(inventory)
        return report

    @staticmethod
    def calculate_products_by_company(inventory: List) -> str:
        company_list = []
        for record in inventory:
            company_list.append(record['nome_da_empresa'])
        c = Counter(company_list)
        c_dict = dict(c)

        result = '\nProdutos estocados por empresa: \n'

        for key in c_dict:
            result += '- ' + key + ': ' + str(c_dict[key]) + '\n'

        return result
