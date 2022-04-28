package com.example.demo.dao.proDao;

import com.example.demo.models.detalleVenModel;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public interface productDao {

    void createProduct(detalleVenModel product);

    List<detalleVenModel> getAllProduct();

    void delProduct(int idPro);

    detalleVenModel getProduct(int idPro);

    void updateProduct(detalleVenModel product);
}
