package com.example.demo.services.serviceTipo;

import com.example.demo.dao.tipDao.tipoDaoImp;
import com.example.demo.models.tipoModel;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
@Service
public class tipoServiceImp implements tipoService{

    String msg="";

    @Autowired
    tipoDaoImp daotipoImp;

    @Override
    public boolean createtipo(tipoModel tipo) {
        if(daotipoImp.gettipo(tipo.getId_tipo())==null) {
            daotipoImp.createtipo(tipo);
            msg = "tipo agregado correctamente";
            System.out.println(msg);
            return true;
        }
        msg = "tipo no agregado";
        System.out.println(msg);
        return false;
    }

    @Override
    public List<tipoModel> getAlltipo() {
        msg = "tipos encontrados";
        System.out.println(msg);
        return daotipoImp.getAlltipo();
    }

    @Override
    public boolean deltipo(int idTipo) {
        if(daotipoImp.gettipo(idTipo)!=null) {
            daotipoImp.deltipo(idTipo);
            msg = "tipo eliminado completamente";
            System.out.println(msg);
            return true;
        }
        msg = "tipo no eliminado";
        System.out.println(msg);
        return false;
    }

    @Override
    public tipoModel gettipo(int idTipo) {
        msg = "tipo encontrado";
        System.out.println(msg);
        return daotipoImp.gettipo(idTipo);
    }

    @Override
    public void updatetipo(tipoModel tipo) {
        if (daotipoImp.gettipo(tipo.getId_tipo())!=null){
            daotipoImp.updatetipo(tipo);
            msg = "tipo encontrado";
        };
        msg = "tipo no encontrado";
        System.out.println(msg);
    }
}
