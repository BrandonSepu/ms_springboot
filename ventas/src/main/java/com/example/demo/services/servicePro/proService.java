package com.example.demo.services.servicePro;

import com.example.demo.models.detalleVenModel;


import java.util.List;

public interface proService {
    boolean createProduct(detalleVenModel product);

    List<detalleVenModel> getAllProduct();

    boolean delProduct(int idPro);

    detalleVenModel getProduct(int idPro);

    void updateProduct(detalleVenModel product);
}
