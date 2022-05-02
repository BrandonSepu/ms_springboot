package com.example.demo.services.serviceTipoPago;

import com.example.demo.dao.proDao.productDaoImp;
import com.example.demo.models.tipoPagoModel;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
@Service
public class tipoPServiceImp implements tipoPService{

    String msg="";

    @Autowired
    productDaoImp daoProImp;

    @Override
    public boolean createtipoPago(tipoPagoModel tipoPago) {
        if(daoProImp.gettipoPago(tipoPago.getid_tpag())==null) {
            daoProImp.createtipoPago(tipoPago);
            msg = "Tipo de pago agregado correctamente";
            System.out.println(msg);
            return true;
        }
        msg = "Tipo de pago no agregado";
        System.out.println(msg);
        return false;
    }

    @Override
    public List<tipoPagoModel> getAlltipoPago() {
        msg = "Tipo de pagos encontrados";
        System.out.println(msg);
        return daoProImp.getAlltipoPago();
    }

    @Override
    public boolean deltipoPago(int id_tpag) {
        if(daoProImp.gettipoPago(id_tpag)!=null) {
            daoProImp.deltipoPago(id_tpag);
            msg = "Tipo de pago eliminado completamente";
            System.out.println(msg);
            return true;
        }
        msg = "Tipo de pago no eliminado";
        System.out.println(msg);
        return false;
    }

    @Override
    public tipoPagoModel gettipoPago(int id_tpag) {
        msg = "Tipo de pago encontrado";
        System.out.println(msg);
        return daoProImp.gettipoPago(id_tpag);
    }

    @Override
    public void updatetipoPago(tipoPagoModel tipoPago) {
        if (daoProImp.gettipoPago(tipoPago.getid_tpag())!=null){
            daoProImp.updatetipoPago(tipoPago);
            msg = "Tipo de pago encontrado";
        };
        msg = "Tipo de pago no encontrado";
        System.out.println(msg);
    }
}
