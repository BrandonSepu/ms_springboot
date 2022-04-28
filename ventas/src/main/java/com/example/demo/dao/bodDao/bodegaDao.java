package com.example.demo.dao.bodDao;

import com.example.demo.models.ventasModel;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public interface bodegaDao {

    void createBodegaPro(ventasModel bodega);

    List<ventasModel> getAllBodegaPro();

    void delBodegaPro(int idBod);

    ventasModel getBodegaPro(int idBod);

    void updateBodegaPro(ventasModel bodega);
}
