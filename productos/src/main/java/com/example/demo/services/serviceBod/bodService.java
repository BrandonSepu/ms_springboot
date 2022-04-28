package com.example.demo.services.serviceBod;

import com.example.demo.models.bodegaModel;


import java.util.List;

public interface bodService {
    boolean createBodegaPro(bodegaModel bodega);

    List<bodegaModel> getAllBodegaPro();

    boolean delBodegaPro(int idBod);

    bodegaModel getBodegaPro(int idBod);

    void updateBodegaPro(bodegaModel bodega);
}
