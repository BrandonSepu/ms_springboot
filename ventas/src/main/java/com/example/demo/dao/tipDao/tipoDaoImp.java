package com.example.demo.dao.tipDao;

import com.example.demo.models.tipoPagoModel;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import javax.transaction.Transactional;
import java.util.List;

@Repository
@Transactional
public class tipoDaoImp implements tipoDao{

    @Autowired
    tipoDaoJpa tipoJpa;

    @Override
    public void createtipo(tipoPagoModel tipo) {
        tipoJpa.save(tipo);
    }

    @Override
    public List<tipoPagoModel> getAlltipo() {
        return tipoJpa.findAll();
    }

    @Override
    public void deltipo(int idTipo) {
        tipoJpa.deleteById(idTipo);
    }

    @Override
    public tipoPagoModel gettipo(int idTipo) {
        try{
            return tipoJpa.findById(idTipo).orElse(null);
        }catch (Exception e){
            e.getMessage();
            return null;
        }
    }

    @Override
    public void updatetipo(tipoPagoModel tipo) {
        tipoJpa.save(tipo);
    }
}
