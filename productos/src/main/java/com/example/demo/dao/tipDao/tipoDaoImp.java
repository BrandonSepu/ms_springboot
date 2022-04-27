package com.example.demo.dao.tipDao;

import com.example.demo.models.tipoModel;
import org.springframework.stereotype.Repository;

import javax.transaction.Transactional;
import java.util.List;

@Repository
@Transactional
public class tipoDaoImp implements tipoDao{
    @Override
    public void createtipo(tipoModel tipo) {

    }

    @Override
    public List<tipoModel> getAlltipo() {
        return null;
    }

    @Override
    public void deltipo(int idTipo) {

    }

    @Override
    public tipoModel gettipo(int idTipo) {
        return null;
    }

    @Override
    public void updatetipo(tipoModel tipo) {

    }
}
