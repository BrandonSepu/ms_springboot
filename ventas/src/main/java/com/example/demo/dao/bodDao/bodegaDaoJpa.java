package com.example.demo.dao.bodDao;

import com.example.demo.models.ventasModel;
import org.springframework.data.jpa.repository.JpaRepository;

public interface bodegaDaoJpa extends JpaRepository<ventasModel, Integer> {

    //@Query("select * from bodega where id_bod = ?")
    //void getById(int id);
}
