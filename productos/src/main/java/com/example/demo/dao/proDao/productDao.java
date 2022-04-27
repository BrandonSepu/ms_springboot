package com.example.demo.dao.proDao;

import com.example.demo.models.productsModel;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public interface productDao {

    void createProduct(productsModel product);

    List<productsModel> getAllProduct();

    void delProduct(int idPro);

    productsModel getProduct(int idPro);

    void updateProduct(productsModel product);
}
