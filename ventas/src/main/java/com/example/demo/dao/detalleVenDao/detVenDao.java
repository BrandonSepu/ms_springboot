package com.example.demo.dao.detalleVenDao;

import com.example.demo.models.detalleVenModel;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public interface detVenDao {

    void createDetVen(detalleVenModel detVen);

    List<detalleVenModel> getAllDetVen();

    void delDetVen(int idDetVen);

    detalleVenModel getDetVen(int idDetVen);

    void updateDetVen(detalleVenModel detVen);
}
