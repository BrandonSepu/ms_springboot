package com.example.demo.dao.proDao;

import com.example.demo.models.detalleVenModel;
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
    public void createProduct(detalleVenModel product) {
        proJpa.save(product);
    }

    @Override
    public List<detalleVenModel> getAllProduct() {
        return proJpa.findAll();
    }

    @Override
    public void delProduct(int idPro) {
        proJpa.deleteById(idPro);
    }

    @Override
    public detalleVenModel getProduct(int idPro) {
        try{
            return proJpa.findById(idPro).orElse(null);
        }catch (Exception e){
            e.getMessage();
            return null;
        }
    }

    @Override
    public void updateProduct(detalleVenModel product) {
        proJpa.save(product);
    }
}
