package com.example.demo.services.serviceDet;

import com.example.demo.dao.ventDao.ventaDaoImp;
import com.example.demo.models.detalleVenModel;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
@Service
public class DetalleServiceImp implements DetalleService{

    String msg="";

    @Autowired
    ventaDaoImp daoBodImp;


    @Override
    public boolean createDetalleVenta(detalleVenModel DetalleVenta) {
        if(daoBodImp.getDetalleVenta(DetalleVenta.getid_detven())==null) {
            daoBodImp.createDetalleVenta(DetalleVenta);
            msg = "Detalle de venta agregado a la bodega correctamente";
            System.out.println(msg);
            return true;
        }
        msg = "Detalle de venta no agregado a la bodega";
        System.out.println(msg);
        return false;

    }

    @Override
    public List<detalleVenModel> getAllDetalleVenta() {
        msg = "Detalles de venta de la bodega encontrados";
        System.out.println(msg);
        return daoBodImp.getAllDetalleVenta();
    }

    @Override
    public boolean delDetalleVenta(int id_detven) {
        if(daoBodImp.getDetalleVenta(id_detven)!=null) {
            daoBodImp.delDetalleVenta(id_detven);
            msg = "Detalle de venta eliminado completamente";
            System.out.println(msg);
            return true;
        }
        msg = "Detalle de venta no eliminado";
        System.out.println(msg);
        return false;

    }

    @Override
    public detalleVenModel getDetalleVenta(int id_detven) {
        msg = "Detalle de venta encontrado";
        System.out.println(msg);
        return daoBodImp.getDetalleVenta(id_detven);
    }

    @Override
    public void updateDetalleVenta(detalleVenModel DetalleVenta) {
        if (daoBodImp.getDetalleVenta(DetalleVenta.id_detven())!=null){
            daoBodImp.updateDetalleVenta(DetalleVenta);
        };
        msg = "Detalle de venta no encontrado";
        System.out.println(msg);
    }
}
