package com.example.demo.dao.ventDao;

import com.example.demo.models.ventasModel;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public interface ventaDao {

    void createVenta(ventasModel venta);

    List<ventasModel> getAllVenta();

    void delBodegaPro(int idBod);

    ventasModel getBodegaPro(int idBod);

    void updateBodegaPro(ventasModel bodega);
}
