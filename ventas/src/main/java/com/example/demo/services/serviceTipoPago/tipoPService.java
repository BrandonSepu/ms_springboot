package com.example.demo.services.servicePro;

import com.example.demo.models.tipoPagoModel;


import java.util.List;

public interface tipoPService {
    boolean createtipoPago(tipoPagoModel tipoPago);

    List<tipoPagoModel> getAlltipoPago();

    boolean deltipoPago(int id_tpag);

    tipoPagoModel gettipoPago(int id_tpag);

    void updatetipoPago(tipoPagoModel tipoPago);
}
