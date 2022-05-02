package com.example.demo.dao.tipoPagoDao;

import com.example.demo.models.tipoPagoModel;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import javax.transaction.Transactional;
import java.util.List;

@Repository
@Transactional
public class tPagoDaoImp implements tPagoDao {

    @Autowired
    tPagoDaoJpa tipoJpa;

    @Override
    public void createTPago(tipoPagoModel tPago) {
        tipoJpa.save(tPago);
    }

    @Override
    public List<tipoPagoModel> getAllTPago() {
        return tipoJpa.findAll();
    }

    @Override
    public void delTPago(int idTPago) {
        tipoJpa.deleteById(idTPago);
    }

    @Override
    public tipoPagoModel getTPago(int idTPago) {
        try{
            return tipoJpa.findById(idTPago).orElse(null);
        }catch (Exception e){
            e.getMessage();
            return null;
        }
    }

    @Override
    public void updateTPago(tipoPagoModel tPago) {
        tipoJpa.save(tPago);
    }
}
