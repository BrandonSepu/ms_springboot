package com.example.demo.services.serviceBod;

import com.example.demo.dao.ventDao.ventaDaoImp;
import com.example.demo.models.ventasModel;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
@Service
public class bodServiceImp implements bodService{

    String msg="";

    @Autowired
    ventaDaoImp daoBodImp;


    @Override
    public boolean createBodegaPro(ventasModel bodega) {
        if(daoBodImp.getBodegaPro(bodega.getId_bod())==null) {
            daoBodImp.createVenta(bodega);
            msg = "producto agregado a la bodega correctamente";
            System.out.println(msg);
            return true;
        }
        msg = "producto no agregado a la bodega";
        System.out.println(msg);
        return false;

    }

    @Override
    public List<ventasModel> getAllBodegaPro() {
        msg = "productos de la bodega encontrados";
        System.out.println(msg);
        return daoBodImp.getAllVenta();
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
    public ventasModel getBodegaPro(int idBod) {
        msg = "producto de bodega encontrado";
        System.out.println(msg);
        return daoBodImp.getBodegaPro(idBod);
    }

    @Override
    public void updateBodegaPro(ventasModel bodega) {
        if (daoBodImp.getBodegaPro(bodega.getId_bod())!=null){
            daoBodImp.updateBodegaPro(bodega);
        };
        msg = "producto de bodega no encontrado";
        System.out.println(msg);
    }
}
