package com.example.demo.dao.proDao;

import com.example.demo.models.productsModel;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import javax.transaction.Transactional;
import java.util.List;

@Repository
@Transactional
public class productDaoImp implements productDao{

    @Autowired
    productDaoJpa proJpa;

    @Override
    public void createProduct(productsModel product) {
        proJpa.save(product);
    }

    @Override
    public List<productsModel> getAllProduct() {
        return proJpa.findAll();
    }

    @Override
    public void delProduct(int idPro) {
        proJpa.deleteById(idPro);
    }

    @Override
    public productsModel getProduct(int idPro) {
        try{
            return proJpa.findById(idPro).orElse(null);
        }catch (Exception e){
            e.getMessage();
            return null;
        }
    }

    @Override
    public void updateProduct(productsModel product) {
        proJpa.save(product);
    }
}
