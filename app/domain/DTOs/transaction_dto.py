from datetime import datetime

from app.domain.DTOs.purchased_product_dto import PurchasedProductDTO


class TransactionDTO:
    def __init__(
        self,
        total_value: float,
        created_at: datetime,
        client_name: str,
        client_cpf: str,
        purchased_products: list[PurchasedProductDTO],
        id: int = None,
    ):
        super().__init__(id)
        self.total_value = total_value
        self.created_at = created_at
        self.clientName = client_name
        self.clientCPF = client_cpf
        self.purchased_products = purchased_products
