package com.example.demo.dao.bodDao;

import com.example.demo.models.bodegaModel;
import org.springframework.stereotype.Repository;

import javax.transaction.Transactional;
import java.util.List;

@Repository
@Transactional
public class bodegaDaoImp implements bodegaDao{
    @Override
    public void createBodegaPro(bodegaModel bodega) {

    }

    @Override
    public List<bodegaModel> getAllBodegaPro() {
        return null;
    }

    @Override
    public void delBodegaPro(int idBod) {

    }

    @Override
    public bodegaModel getBodegaPro(int idBod) {
        return null;
    }

    @Override
    public void updateBodegaPro(bodegaModel bodega) {

    }
}
