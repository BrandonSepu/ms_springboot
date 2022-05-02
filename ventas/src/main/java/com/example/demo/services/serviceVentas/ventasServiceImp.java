package com.example.demo.services.serviceVentas;

import com.example.demo.dao.ventDao.VentaDaoImp;
import com.example.demo.models.ventasModel;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
@Service
public class ventasServiceImp implements ventasService{

    String msg="";

    @Autowired
    VentaDaoImp daoVenImp;

    @Override
    public boolean createventas(ventasModel ventas) {
        if(daoVenImp.getVenta(ventas.getId_ventas())==null) {
            daoVenImp.createVenta(ventas);
            msg = "ventas agregadas correctamente";
            System.out.println(msg);
            return true;
        }
        msg = "ventas no agregadas";
        System.out.println(msg);
        return false;
    }

    @Override
    public List<ventasModel> getAllventas() {
        msg = "ventas encontradas";
        System.out.println(msg);
        return daoVenImp.getAllVenta();
    }

    @Override
    public boolean delventas(int id_ventas) {
        if(daoVenImp.getVenta(id_ventas)!=null) {
            daoVenImp.delVenta(id_ventas);
            msg = "ventas eliminadas completamente";
            System.out.println(msg);
            return true;
        }
        msg = "ventas no eliminadas";
        System.out.println(msg);
        return false;
    }

    @Override
    public ventasModel getventas(int id_ventas) {
        msg = "ventas encontradas";
        System.out.println(msg);
        return daoVenImp.getVenta(id_ventas);
    }

    @Override
    public void updateventas(ventasModel ventas) {
        if (daoVenImp.getVenta(ventas.getId_ventas())!=null){
            daoVenImp.updateVenta(ventas);
            msg = "ventas encontradas";
        };
        msg = "ventas no encontradas";
        System.out.println(msg);
    }

}
