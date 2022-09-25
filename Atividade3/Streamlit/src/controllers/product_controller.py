from src.models.product import Product

class ProductController():
    def __init__(self):
        self.produtos = [
            Product(name = "Cadeira", price = 99.90, url ="https://images.tcdn.com.br/img/img_prod/1067049/cadeira_estofado_dinner_casa_cristallo_1343_1_b71d617c6db683d27f193fc6acf7696d.png"),
            Product(name = "Boné", price = 22.90, url = "https://d1taioma509ygp.cloudfront.net/Custom/Content/Products/64/27/64272_bone-oakley-tincan-safari-pr-4092-911545-31s_m1_637395084046183736.png"),
            Product(name = "RTX4090", price = 14990.00, url = "https://asset.msi.com/resize/image/global/product/product_1663823505047319e6ab23cf7b4de59b8151e906f9.png62405b38c58fe0f07fcef2367d8a9ba1/1024.png"),
            Product(name = "Dark Souls (PC)", price = 99.90 , url = "https://upload.wikimedia.org/wikipedia/pt/7/7c/Dark_Souls_1_capa.png")
        ]

    def get_product(self,index):
        return self.produtos[index]
