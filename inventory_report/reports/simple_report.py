from typing import Counter, List
from datetime import datetime


class SimpleReport():
    @staticmethod
    def generate(inventory: List) -> str:
        report = 'Data de fabricação mais antiga: ' + \
            SimpleReport.calculate_earliest_manufacture_date(inventory)
        report += 'Data de validade mais próxima: ' + \
            SimpleReport.calculate_closest_expiration_date(inventory)
        report += 'Empresa com maior quantidade de produtos estocados: ' + \
            SimpleReport.calculate_company_greatest_amount_products(inventory)
        return report

    @staticmethod
    def calculate_earliest_manufacture_date(inventory: List) -> str:
        earliest_date = datetime.today()
        for record in inventory:
            manufacture_date = datetime.strptime(record['data_de_fabricacao'],
                                                 '%Y-%m-%d')
            if manufacture_date < earliest_date:
                earliest_date = manufacture_date
        return earliest_date.strftime('%Y-%m-%d') + '\n'

    @staticmethod
    def calculate_closest_expiration_date(inventory: List) -> str:
        today = datetime.today()
        closest_expiration: datetime = datetime.today()
        first_iteration = True
        for record in inventory:
            if first_iteration:
                closest_expiration = datetime.strptime(record['data' +
                                                       '_de_validade'],
                                                       '%Y-%m-%d')
                first_iteration = False
                continue
            expiration_date = datetime.strptime(record['data_de_validade'],
                                                '%Y-%m-%d')
            if today <= expiration_date <= closest_expiration:
                closest_expiration = expiration_date
        return closest_expiration.strftime('%Y-%m-%d') + '\n'

    @staticmethod
    def calculate_company_greatest_amount_products(inventory: List) -> str:
        company_list = []
        for record in inventory:
            company_list.append(record['nome_da_empresa'])
        c = Counter(company_list)
        return c.most_common(1)[0][0] + '\n'
