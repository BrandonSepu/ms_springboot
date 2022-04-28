package com.example.demo.dao.proDao;

import com.example.demo.models.detalleVenModel;
import org.springframework.data.jpa.repository.JpaRepository;

public interface productDaoJpa extends JpaRepository<detalleVenModel, Integer> {

    //@Query("select * from productos where id_pro = ?")
    //void getById(int id);
}
