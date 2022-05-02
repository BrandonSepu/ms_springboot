package com.example.demo.services.serviceDet;

import com.example.demo.models.detalleVenModel;


import java.util.List;

public interface DetalleService {
    boolean createDetalleVenta(detalleVenModel DetalleVenta);

    List<detalleVenModel> getAllDetalleVenta();

    boolean delDetalleVenta(int id_detven);

    detalleVenModel getDetalleVenta(int id_detven);

    void updateDetalleVenta(detalleVenModel venta);
}
