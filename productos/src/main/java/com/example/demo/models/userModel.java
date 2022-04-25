package com.example.demo.models;

import javax.persistence.*;
import java.io.Serializable;

@Entity
@Table(name="USER")
//@NamedQuery(name="user.findAll", query="SELECT u FROM user u")
public class userModel implements Serializable {
    private static final long serialVersionUID = 1L;

    @Id
    @GeneratedValue(strategy= GenerationType.IDENTITY)
    @Column(name = "id_user")
    private int id_user;
    @Column(name = "nom_user")
    private String nom_user;
    @Column(name = "rut_user")
    private String rut_user;
    @Column(name = "age_user")
    private int age_user;
    @Column(name = "tipo_user")
    private String tipo_user;
    @Column(name = "email_user")
    private String email_user;
    @Column(name = "pass_user")
    private String pass_user;

    public userModel() {

    }

    public userModel(String nom_user, String rut_user, int age_user, String tipo_user, String email_user, String pass_user) {
        this.nom_user = nom_user;
        this.rut_user = rut_user;
        this.age_user = age_user;
        this.tipo_user = tipo_user;
        this.email_user = email_user;
        this.pass_user = pass_user;
    }

    public int getId_user() {
        return id_user;
    }

    public void setId_user(Integer id_user) {
        this.id_user = id_user;
    }

    public String getNom_user() {
        return nom_user;
    }

    public void setNom_user(String nom_user) {
        this.nom_user = nom_user;
    }

    public String getRut_user() {
        return rut_user;
    }

    public void setRut_user(String rut_user) {
        this.rut_user = rut_user;
    }

    public int getAge_user() {
        return age_user;
    }

    public void setAge_user(Integer age_user) {
        this.age_user = age_user;
    }

    public String getTipo_user() {
        return tipo_user;
    }

    public void setTipo_user(String tipo_user) {
        this.tipo_user = tipo_user;
    }

    public String getEmail_user() {
        return email_user;
    }

    public void setEmail_user(String email_user) {
        this.email_user = email_user;
    }

    public String getPass_user() {
        return pass_user;
    }

    public void setPass_user(String pass_user) {
        this.pass_user = pass_user;
    }
}
