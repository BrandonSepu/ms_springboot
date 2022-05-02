package com.example.demo.services.serviceTipo;

import com.example.demo.dao.tipoPagoDao.tPagoDaoImp;
import com.example.demo.models.tipoPagoModel;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
@Service
public class tipoServiceImp implements tipoService{

    String msg="";

    @Autowired
    tPagoDaoImp daotipoImp;

    @Override
    public boolean createtipo(tipoPagoModel tipo) {
        if(daotipoImp.getTPago(tipo.getId_tipo())==null) {
            daotipoImp.createTPago(tipo);
            msg = "tipo agregado correctamente";
            System.out.println(msg);
            return true;
        }
        msg = "tipo no agregado";
        System.out.println(msg);
        return false;
    }

    @Override
    public List<tipoPagoModel> getAlltipo() {
        msg = "tipos encontrados";
        System.out.println(msg);
        return daotipoImp.getAllTPago();
    }

    @Override
    public boolean deltipo(int idTipo) {
        if(daotipoImp.getTPago(idTipo)!=null) {
            daotipoImp.delTPago(idTipo);
            msg = "tipo eliminado completamente";
            System.out.println(msg);
            return true;
        }
        msg = "tipo no eliminado";
        System.out.println(msg);
        return false;
    }

    @Override
    public tipoPagoModel gettipo(int idTipo) {
        msg = "tipo encontrado";
        System.out.println(msg);
        return daotipoImp.getTPago(idTipo);
    }

    @Override
    public void updatetipo(tipoPagoModel tipo) {
        if (daotipoImp.getTPago(tipo.getId_tipo())!=null){
            daotipoImp.updateTPago(tipo);
            msg = "tipo encontrado";
        };
        msg = "tipo no encontrado";
        System.out.println(msg);
    }
}
