package com.example.demo.dao.bodDao;

import com.example.demo.models.ventasModel;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import javax.transaction.Transactional;
import java.util.List;

@Repository
@Transactional
public class bodegaDaoImp implements bodegaDao{

    @Autowired
    bodegaDaoJpa bodJpa;

    @Override
    public void createBodegaPro(ventasModel bodega) {
        bodJpa.save(bodega);
    }

    @Override
    public List<ventasModel> getAllBodegaPro() {
        return bodJpa.findAll();
    }

    @Override
    public void delBodegaPro(int idBod) {
        bodJpa.deleteById(idBod);
    }

    @Override
    public ventasModel getBodegaPro(int idBod) {
        try{
            return bodJpa.findById(idBod).orElse(null);
        }catch (Exception e){
            e.getMessage();
            return null;
        }
    }

    @Override
    public void updateBodegaPro(ventasModel bodega) {
        bodJpa.save(bodega);
    }
}
