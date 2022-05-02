package com.example.demo.services.serviceVentas;

import com.example.demo.dao.tipDao.tipoDaoImp;
import com.example.demo.models.ventasModel;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
@Service
public class ventasServiceImp implements ventasService{

    String msg="";

    @Autowired
    tipoDaoImp daotipoImp;

    @Override
    public boolean createventas(ventasModel ventas) {
        if(daotipoImp.getventas(ventas.getid_ventas())==null) {
            daotipoImp.createventas(ventas);
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
        return daotipoImp.getAllventas();
    }

    @Override
    public boolean delventas(int id_ventas) {
        if(daotipoImp.getventas(id_ventas)!=null) {
            daotipoImp.delventas(id_ventas);
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
        return daotipoImp.getventas(id_ventas);
    }

    @Override
    public void updateventas(ventasModel ventas) {
        if (daotipoImp.getventas(ventas.getid_ventas())!=null){
            daotipoImp.updateventas(ventas);
            msg = "ventas encontradas";
        };
        msg = "ventas no encontradas";
        System.out.println(msg);
    }

    @Override
    public List<ventasModel> getAlltipo() {
        // TODO Auto-generated method stub
        return null;
    }
}
