package com.example.demo.dao.bodDao;

import com.example.demo.models.bodegaModel;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public interface bodegaDao {

    void createBodegaPro(bodegaModel bodega);

    List<bodegaModel> getAllBodegaPro();

    void delBodegaPro(int idBod);

    bodegaModel getBodegaPro(int idBod);

    void updateBodegaPro(bodegaModel bodega);
}
