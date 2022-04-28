package com.example.demo.dao.tipDao;

import com.example.demo.models.tipoPagoModel;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public interface tipoDao {
    void createtipo(tipoPagoModel tipo);

    List<tipoPagoModel> getAlltipo();

    void deltipo(int idTipo);

    tipoPagoModel gettipo(int idTipo);

    void updatetipo(tipoPagoModel tipo);
}
