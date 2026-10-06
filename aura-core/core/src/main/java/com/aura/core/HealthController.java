package com.aura.core;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/api/v1/health")
public class HealthController {

    @GetMapping
    public Map<String, Object> getHealthStatus() {
        Map<String, Object> status = new HashMap<>();
        status.put("system", "AURA Enterprise OS - Core Ledger");
        status.put("status", "UP");
        status.put("timestamp", System.currentTimeMillis());
        status.put("database", "Connected to Supabase PostgreSQL");
        return status;
    }
}