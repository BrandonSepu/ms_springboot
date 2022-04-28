package com.example.demo.services.serviceBod;

import com.example.demo.dao.bodDao.bodegaDaoImp;
import com.example.demo.models.bodegaModel;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
@Service
public class bodServiceImp implements bodService{

    String msg="";

    @Autowired
    bodegaDaoImp daoBodImp;


    @Override
    public boolean createBodegaPro(bodegaModel bodega) {
        if(daoBodImp.getBodegaPro(bodega.getId_bod())==null) {
            daoBodImp.createBodegaPro(bodega);
            msg = "producto agregado a la bodega correctamente";
            System.out.println(msg);
            return true;
        }
        msg = "producto no agregado a la bodega";
        System.out.println(msg);
        return false;

    }

    @Override
    public List<bodegaModel> getAllBodegaPro() {
        msg = "productos de la bodega encontrados";
        System.out.println(msg);
        return daoBodImp.getAllBodegaPro();
    }

    @Override
    public boolean delBodegaPro(int idBod) {
        if(daoBodImp.getBodegaPro(idBod)!=null) {
            daoBodImp.delBodegaPro(idBod);
            msg = "producto de a bodega eliminado completamente";
            System.out.println(msg);
            return true;
        }
        msg = "producto de la bodega no eliminado";
        System.out.println(msg);
        return false;

    }

    @Override
    public bodegaModel getBodegaPro(int idBod) {
        msg = "producto de bodega encontrado";
        System.out.println(msg);
        return daoBodImp.getBodegaPro(idBod);
    }

    @Override
    public void updateBodegaPro(bodegaModel bodega) {
        if (daoBodImp.getBodegaPro(bodega.getId_bod())!=null){
            daoBodImp.updateBodegaPro(bodega);
        };
        msg = "producto de bodega no encontrado";
        System.out.println(msg);
    }
}
