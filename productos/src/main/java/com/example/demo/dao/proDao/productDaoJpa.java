package com.example.demo.dao.proDao;

import com.example.demo.models.productsModel;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

public interface productDaoJpa extends JpaRepository<productsModel, Integer> {

    //@Query("select * from productos where id_pro = ?")
    //void getById(int id);
}
