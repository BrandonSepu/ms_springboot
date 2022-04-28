package com.example.demo.services.serviceTipo;

import com.example.demo.models.tipoPagoModel;


import java.util.List;

public interface tipoService {
    boolean createtipo(tipoPagoModel tipo);

    List<tipoPagoModel> getAlltipo();

    boolean deltipo(int idTipo);

    tipoPagoModel gettipo(int idTipo);

    void updatetipo(tipoPagoModel tipo);
}
