package com.example.demo.services.servicePro;

import com.example.demo.dao.detalleVenDao.detVenDaoImp;
import com.example.demo.models.detalleVenModel;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
@Service
public class proServiceImp implements proService{

    String msg="";

    @Autowired
    detVenDaoImp daoProImp;

    @Override
    public boolean createProduct(detalleVenModel product) {
        if(daoProImp.getDetVen(product.getId_pro())==null) {
            daoProImp.createDetVen(product);
            msg = "producto agregado correctamente";
            System.out.println(msg);
            return true;
        }
        msg = "producto no agregado";
        System.out.println(msg);
        return false;
    }

    @Override
    public List<detalleVenModel> getAllProduct() {
        msg = "productos encontrados";
        System.out.println(msg);
        return daoProImp.getAllDetVen();
    }

    @Override
    public boolean delProduct(int idPro) {
        if(daoProImp.getDetVen(idPro)!=null) {
            daoProImp.delDetVen(idPro);
            msg = "producto eliminado completamente";
            System.out.println(msg);
            return true;
        }
        msg = "producto no eliminado";
        System.out.println(msg);
        return false;
    }

    @Override
    public detalleVenModel getProduct(int idPro) {
        msg = "producto encontrado";
        System.out.println(msg);
        return daoProImp.getDetVen(idPro);
    }

    @Override
    public void updateProduct(detalleVenModel product) {
        if (daoProImp.getDetVen(product.getId_pro())!=null){
            daoProImp.updateDetVen(product);
            msg = "producto encontrado";
        };
        msg = "producto no encontrado";
        System.out.println(msg);
    }
}
