package com.example.demo.dao.tipoPagoDao;

import com.example.demo.models.tipoPagoModel;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public interface tPagoDao {
    void createTPago(tipoPagoModel tPago);

    List<tipoPagoModel> getAllTPago();

    void delTPago(int idTPago);

    tipoPagoModel getTPago(int idTPago);

    void updateTPago(tipoPagoModel tPago);
}
