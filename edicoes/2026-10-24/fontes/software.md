# AWS Introduces Lambda Web Functions for Node.js Applications

- Editoria: Software (`software`)
- Fonte: InfoQ — https://www.infoq.com/news/2026/10/aws-lambda-web-functions/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
- Autor: Renato Losio
- Publicado: 2026-10-23T12:49:00+00:00
- Score: 5.541
- Imagem: imagens/software-aws-introduces-lambda-web-functions-for.jpg | crédito: InfoQ | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- nenhuma

## Texto extraído

AWS recently introduced Lambda Web Functions, allowing developers to run Node.js web applications using frameworks such as Express and Hono directly on Lambda, with support for concurrent requests and response streaming.
According to the Lambda Web Functions documentation, the new functions support concurrent HTTP requests and response streaming. They charge for active CPU time and memory, rather than CPU time spent waiting for downstream services. Multi-Region routing directs requests to the closest Region, while a single warm execution environment can handle multiple concurrent requests, significantly reducing cold starts. Existing Lambda functions are now called Lambda Event Functions, with no changes required. Micah Walter, senior solutions architect at AWS, summarizes the benefits and why it removes this complexity:
You can take a standard port-listening server built with Express, Hono, Fastify, Next.js, or any Node.js framework, deploy it with a single command, and Lambda automatically handles scaling, multi-region distribution, and active CPU billing. No adapters, no infrastructure to manage, and no framework lock-in.
Endpoints use a Lambda-provided domain by default. To use a custom domain, edge caching, or AWS WAF, developers can use Amazon CloudFront in front, relying on Lambda Web Functions as the origin.
Lambda Web Functions target HTTP workloads, including full-stack web applications, REST and GraphQL APIs, and independently scaling microservices. They also support server-side rendering and streaming responses, such as incremental output from large language models, without requiring a separate hosting layer.
Lambda Web Functions currently support only Node.js; other languages, including Python, Java, and .NET, remain available through traditional Lambda functions. Earlier this year, AWS also launched Lambda MicroVMs, which provide isolated, stateful sandbox environments for running untrusted or user-generated code, with customer-managed lifecycles.
In their article "Exploring AWS Lambda Web Functions for Building Web Applications", Julian Wood, Kim Wendt, and Samrat Karak build a sample application to show how one execution environment handles many requests at once and how the application serves users globally. They summarize:
Lambda Web Functions bring the serverless operating model to web applications without adapter layers. You write a standard Node.js HTTP server, deploy it with one command or CloudFormation, and get a scalable, pay-per-use HTTPS endpoint with global routing built in.
Community reactions on Reddit and Hacker News have been largely positive, highlighting the simpler programming model and support for concurrent requests. However, discussions also raise questions about Python support and how the service differs from existing alternatives. User magnetik79 comments:
This is a big one - and nice to see something not entirely honed in AI. ☺️ What looks great: Many workloads can now skip API Gateway entirely (...) this totally changes the current Lambda HTTP programming model - now you're no longer working with one invoke/one request - now you might need to be sync/mutex aware.
In his article "Why I'm Excited About AWS Lambda Web Functions," Eric Johnson, principal developer advocate at AWS, highlights how Lambda Web Functions run standard HTTP servers and frameworks without modification, supporting REST, server-sent events, streaming responses, RPC, webhooks, and IAM authentication through a single managed endpoint.
AWS is not the only cloud provider offering this model: Google Cloud Run and Azure Container Apps also support web applications without adapter layers, scale-to-zero, and configurable concurrency, making them suitable for workloads with intermittent or bursty traffic.
Pricing for Lambda Web Functions is based on active CPU time and memory usage, potentially reducing costs for workloads that spend time waiting on databases or APIs. Memory is billed for the lifetime of the execution environment. This model may benefit I/O-heavy workloads, such as server-side rendering, API backends, and streaming AI inference. The service is currently available in five regions: Northern Virginia, Ohio, Oregon, Tokyo, and Ireland.
