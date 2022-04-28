package com.example.demo.services.servicePro;

import com.example.demo.models.productsModel;


import java.util.List;

public interface proService {
    boolean createProduct(productsModel product);

    List<productsModel> getAllProduct();

    boolean delProduct(int idPro);

    productsModel getProduct(int idPro);

    void updateProduct(productsModel product);
}
