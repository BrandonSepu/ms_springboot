package com.example.demo.dao.detalleVenDao;

import com.example.demo.models.detalleVenModel;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import javax.transaction.Transactional;
import java.util.List;

@Repository
@Transactional
public class detVenDaoImp implements detVenDao {

    @Autowired
    detVenDaoJpa proJpa;

    @Override
    public void createDetVen(detalleVenModel detVen) {
        proJpa.save(detVen);
    }

    @Override
    public List<detalleVenModel> getAllDetVen() {
        return proJpa.findAll();
    }

    @Override
    public void delDetVen(int idDetVen) {
        proJpa.deleteById(idDetVen);
    }

    @Override
    public detalleVenModel getDetVen(int idDetVen) {
        try{
            return proJpa.findById(idDetVen).orElse(null);
        }catch (Exception e){
            e.getMessage();
            return null;
        }
    }

    @Override
    public void updateDetVen(detalleVenModel detVen) {
        proJpa.save(detVen);
    }
}
