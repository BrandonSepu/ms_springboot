package com.example.demo.services.servicePro;

import com.example.demo.dao.proDao.productDaoImp;
import com.example.demo.models.productsModel;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
@Service
public class proServiceImp implements proService{

    String msg="";

    @Autowired
    productDaoImp daoProImp;

    @Override
    public boolean createProduct(productsModel product) {
        if(daoProImp.getProduct(product.getId_pro())==null) {
            daoProImp.createProduct(product);
            msg = "producto agregado correctamente";
            System.out.println(msg);
            return true;
        }
        msg = "producto no agregado";
        System.out.println(msg);
        return false;
    }

    @Override
    public List<productsModel> getAllProduct() {
        msg = "productos encontrados";
        System.out.println(msg);
        return daoProImp.getAllProduct();
    }

    @Override
    public boolean delProduct(int idPro) {
        if(daoProImp.getProduct(idPro)!=null) {
            daoProImp.delProduct(idPro);
            msg = "producto eliminado completamente";
            System.out.println(msg);
            return true;
        }
        msg = "producto no eliminado";
        System.out.println(msg);
        return false;
    }

    @Override
    public productsModel getProduct(int idPro) {
        msg = "producto encontrado";
        System.out.println(msg);
        return daoProImp.getProduct(idPro);
    }

    @Override
    public void updateProduct(productsModel product) {
        if (daoProImp.getProduct(product.getId_pro())!=null){
            daoProImp.updateProduct(product);
            msg = "producto encontrado";
        };
        msg = "producto no encontrado";
        System.out.println(msg);
    }
}
