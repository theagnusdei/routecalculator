# FirstQFM Model Cuts Single-Qubit Gate Times by 33% on QuantWare Processor

- Editoria: Engenharia e Computação Quântica (`quantica`)
- Fonte: The Quantum Insider — https://thequantuminsider.com/2026/10/15/firstqfm-model-cuts-single-qubit-gate-times-33-percent-quantware/
- Autor: Mohib Ur Rehman
- Publicado: 2026-10-15T09:21:07+00:00
- Score: 5.713
- Imagem: imagens/quantica-firstqfm-model-cuts-single-qubit-gate-ti.jpg | crédito: The Quantum Insider | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- nenhuma

## Texto extraído

Insider Brief
- FirstQFM applied its quantum foundation model to a 21-qubit QuantWare superconducting processor at the Israeli Quantum Computing Center, reducing single-qubit gate execution time by 33% without reducing gate fidelity.
- The model generated custom pulse-level gate implementations from existing calibration data and identified five qubit pairs with improved Bell-state fidelity, with the improvements confirmed in independent hardware runs.
- The work used Quantum Machines’ control and calibration infrastructure alongside NVIDIA accelerated computing, and FirstQFM plans to expand its optimizations as QuantWare develops larger quantum processors.
PRESS RELEASE — FirstQFM today announced results from applying FirstQFM’s quantum foundation model to a QuantWare superconducting quantum processor at the Israeli Quantum Computing Center (IQCC).
FirstQFM’s foundation model builds on top of Quantum Machines’ native calibration stack, and generated single-qubit gates that reduced execution time by 33% on a QuantWare Contralto-D21 QPU. Gates were validated directly on the QuantWare processor using randomized benchmarking with no loss of gate fidelity. The model generated custom pulse-level implementations of gates from calibration data produced by the Quantum Machines’ calibration stack with no additional quantum hardware measurements required. This shifts more of the gate optimization process from scarce QPU time to classical compute.
The model also identified improvements to two-qubit gates, which are central to entanglement and typically more challenging to calibrate than single-qubit operations. Using existing calibration data together with a short hardware probe, the model identified five qubit pairs with higher Bell-state fidelity with each improvement confirmed in independent hardware runs.
The QuantWare processor was operated at the IQCC using Quantum Machines’ OPX control hardware, QUA software, and automated calibration infrastructure. FirstQFM developed its foundation model using NVIDIA accelerated computing hardware and software, including the Leonardo supercomputer and the NVIDIA CUDA-Q open source hybrid platform, before fine-tuning and applying the model to the QuantWare processor.
“FirstQFM’s proprietary, patented foundation models are built to learn the operating characteristics of quantum hardware and use that information to improve how the system performs,” said Vish Ramakrishnan, CEO and Co-Founder of FirstQFM. “On QuantWare’s processor, our model was able to use existing calibration data to generate shorter single-qubit gates while preserving fidelity, and to improve selected two-qubit operations.”
As superconducting quantum processors grow, calibration becomes a harder control problem. More qubits and couplers introduce more operating parameters, device interactions, crosstalk and drift to characterize and manage. FirstQFM plans to expand the set of optimizations available for the 21-qubit device while scaling the solution in preparation for QuantWare advances toward larger VIO-based QPUs.
