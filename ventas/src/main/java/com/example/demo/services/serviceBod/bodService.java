package com.example.demo.services.serviceBod;

import com.example.demo.models.ventasModel;


import java.util.List;

public interface bodService {
    boolean createBodegaPro(ventasModel bodega);

    List<ventasModel> getAllBodegaPro();

    boolean delBodegaPro(int idBod);

    ventasModel getBodegaPro(int idBod);

    void updateBodegaPro(ventasModel bodega);
}
