package com.enterpriseai.controller;

import com.enterpriseai.service.AiApiService;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@WebMvcTest(AiController.class)
class AiControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private AiApiService aiApiService;

    @Test
    @DisplayName("GET /predict/{teamSize}/{issues} returns prediction map")
    void testPredict() throws Exception {
        Map<String, Object> mockResponse = new HashMap<>();
        mockResponse.put("predicted_duration", 10);
        mockResponse.put("predicted_cost", 5000);
        mockResponse.put("delay_risk", true);

        when(aiApiService.predictFull(5, 3)).thenReturn(mockResponse);

        mockMvc.perform(get("/predict/5/3"))
                .andExpect(status().isOk())
                .andExpect(content().contentType(MediaType.APPLICATION_JSON))
                .andExpect(jsonPath("$.predicted_duration").value(10))
                .andExpect(jsonPath("$.predicted_cost").value(5000))
                .andExpect(jsonPath("$.delay_risk").value(true));
    }

    @Test
    @DisplayName("GET /projects returns all projects")
    void testGetProjects() throws Exception {
        List<Map<String, Object>> mockProjects = List.of(
            Map.of(
                "id", 1,
                "team_size", 5,
                "issues", 2,
                "predicted_duration", 80,
                "predicted_cost", 40000,
                "delay_risk", false
            )
        );

        when(aiApiService.getProjects()).thenReturn(mockProjects);

        mockMvc.perform(get("/projects")
                .accept(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$[0].team_size").value(5));
    }

    @Test
    @DisplayName("GET /predict returns 500 when ML API fails")
    void testPredictFailure() throws Exception {
        when(aiApiService.predictFull(5, 3))
                .thenThrow(new RuntimeException("ML API down"));

        mockMvc.perform(get("/predict/5/3"))
                .andExpect(status().is5xxServerError());
    }

}
