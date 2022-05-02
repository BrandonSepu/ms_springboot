package com.example.demo.services.serviceVentas;

import com.example.demo.models.ventasModel;


import java.util.List;

public interface ventasService {

    boolean createventas(ventasModel ventas);

    List<ventasModel> getAllventas();

    boolean delventas(int id_ventas);

    ventasModel getventas(int id_ventas);

    void updateventas(ventasModel ventas);
}
