package com.example.demo.dao;

import com.example.demo.models.userModel;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Component;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Component
public interface userDaoJpa extends JpaRepository<userModel, Integer> {

    //userModel findByEmail(int id);
    //@Transactional
    //@Modifying
    //@Query("select u FROM USER u WHERE u.rut_user =?1")
    //List<userModel> getByRut(String rut_user);
}
