package com.example.demo.dao.proDao;

import com.example.demo.models.productsModel;
import org.springframework.stereotype.Repository;

import javax.transaction.Transactional;
import java.util.List;

@Repository
@Transactional
public class productDaoImp implements productDao{
    @Override
    public void createProduct(productsModel product) {

    }

    @Override
    public List<productsModel> getAllProduct() {
        return null;
    }

    @Override
    public void delProduct(int idPro) {

    }

    @Override
    public productsModel getProduct(int idPro) {
        return null;
    }

    @Override
    public void updateProduct(productsModel product) {

    }
}
