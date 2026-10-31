# Spring News Roundup: First Release Candidates of Boot, Framework, Data, Security, Modulith, AI

- Editoria: Software (`software`)
- Fonte: InfoQ — https://www.infoq.com/news/2026/10/spring-news-roundup-oct19-2026/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
- Autor: Michael Redlich
- Publicado: 2026-10-31T13:30:00+00:00
- Score: 6.498
- Imagem: imagens/software-spring-news-roundup-first-release-candid.jpg | crédito: InfoQ | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- nenhuma

## Texto extraído

There was a flurry of activity during the week of October 19th, 2026, highlighting: first release candidates of: Spring Boot, Spring Framework, Spring Data, Spring Cloud, Spring Security, Spring for GraphQL, Spring Session, Spring Integration, Spring HATEOS, Spring Modulith, Spring REST Docs, Spring AI, Spring Batch, Spring AMQP, Spring for Apache Kafka, Spring LDAP and Spring Web Services.
Spring Boot
The first release candidate of Spring Boot 4.2.0 delivers bug fixes, documentation improvements, dependency upgrades and new features such as: a migration to the Ubuntu Resolute builder replacing the Noble Java Tiny Builder; and improved Uber-Jar performance using direct lookup of classes and resources in nested jars. More details on this release may be found in the release notes and this wiki page.
Spring Framework
The first release candidate of Spring Framework 7.1.0 ships with bug fixes, dependency upgrades and new features such as: improved nullability in the DataAccessUtils and LinkedCaseInsensitiveMap classes; and new overloaded methods, onRetrySuccess() and onRetryFailure(), defined in the RetryListener interface, that add an instance of the RetryState class in the parameter list such that listeners can access the retry state directly upon failure. Further details on this release, including removal of deprecated APIs, may be found in the release notes.
Spring Data
The first release candidate of Spring Data 2026.1.0 provides bug fixes, dependency upgrades, RC1 upgrades to all of the subprojects and a notable new feature in Spring Data Redis that now forwards subscription notifications related to annotated listener methods if a bean implements the SubscriptionListener interface.
Spring Cloud
The first release candidate of Spring Cloud 2026.0.0, codenamed Paddington, delivers dependency upgrades, RC1 upgrades to all of the subprojects and a notable change where Spring Cloud Bus is no longer its own project and has been incorporated into Spring Cloud Stream. This release is based on Spring Boot 4.2.0-RC1. More details on this release may be found in this release notes.
Spring Security
The first release candidate of Spring Security 7.2.0 ships with bug fixes, dependency upgrades and two new features: an instance of the StrictServerWebExchangeFirewall class no longer detects a non-canonical-case HTTP method as a distinct value due to a change in the valueOf() method, defined in the Spring Framework HttpMethod class, that now normalizes casing; and RestClientOpaqueTokenIntrospector and SpringOpaqueTokenIntrospector classes now set the Content-Type header to application/x-www-form-urlencoded. Further details on this release may be found in the release notes and this what's new page.
Spring for GraphQL
The first release candidate of Spring for GraphQL 2.1.0 provides one bug fix that reinstates the Content-Length response header for WebFlux applications so that backwards compatibility is maintained and notable dependency upgrades such as: Spring Framework 7.1.0-RC1; Spring Data 2026.1.0-RC1; and Spring Security 7.2.0-RC1. More details on this release may be found in the release notes.
Spring Session
The first release candidate of Spring Session 4.2.0 delivers bug fixes, dependency upgrades and new features such as: integrating the Spring Security Settings Plugin and Spring Security Maven Plugin; and standardizing the configuration of the public and private continuous integration environments. Further details on this release may be found in the release notes.
Spring Integration
The first release candidate of Spring Integration 7.2.0 ships with bug fixes, documentation improvements, dependency upgrades and new features such as: a deprecation of the default constructor in the SerializingHttpMessageConverter class to define a new constructor that contains the allowedPatterns attribute for improved security; and the ability to allow the DefaultJmsHeaderMapper class to set the outboundHeaderNames, inboundHeaderNames and excludedOutboundStandardRequestHeaderNames and excludedInboundStandardResponseHeaderNames to align with the DefaultHttpHeaderMapper class. More details on this release may be found in the release notes.
Spring HATEOAS
The first release candidate of Spring HATEOAS 3.2.0 provides notable dependency upgrades such as: Spring Framework 7.1.0-RC1; Spring Plugin 4.2.0-RC1; and Reactor 2026.0.0-RC1. Further details on this release may be found in the release notes.
Spring Modulith
The first release candidate of Spring Modulith 2.2.0 delivers bug fixes, dependency upgrades and new features such as: new ABANDONED and RESUBMITTED enumerations, added to the EventPublication.Status interface, to distinguish between failed and abandoned event publications; and event publications are now completed, by default, using the Spring Framework TransactionSynchronization interface within a listener's transaction to avoid the possibility of a listener committing and the completion to fail. More details on this release may be found in the release notes.
Spring REST Docs
The first release candidate of Spring REST Docs 4.1.0 ships with one bug fix, a dependency upgrade to Spring Framework 7.1.0-RC1 and new features such as: improved nullability using JSpecify; and support for using the Spring Framework RestTestClient interface. Further details on this release may be found in the release notes.
Spring AI
The first release candidate of Spring AI 2.1.0 provides dependency upgrades and new features such as: a new SessionService interface for creating and finding sessions that replaces the now-deprecated ChatMemory interface; and the ability for the OpenAiChatModel and DeepSeekChatModel classes to build an assistant message of each choice from ordered message parts. More details on this release may be found in the release notes.
Spring Batch
The first release candidate of Spring Batch 6.1.0 delivers bug fixes, documentation improvements, dependency upgrades and new features such as: a new @JobParameter annotation that injects a job parameter into a job or step scoped bean used to require a Spring Expression Language (SpEL) expression; and a new PageableItemReader class that serves as a type-safe alternative to RepositoryItemReader class to take a function from the Spring Data Pageable interface to a Slice interface. Further details on this release may be found in the release notes.
Spring AMQP
The first release candidate of Spring AMQP 4.2.0 ships with bug fixes, documentation improvements, dependency upgrades and new features such as: removal of the use of the noNullElements() method, defined in the Spring Framework Assert class, to allow the RabbitAdmin class and AmqpAdmin interface to accept null or empty arrays when declaring exchanges, queues, and bindings; and a simplification of the buildMessage() method, defined in both the AbstractAdaptableMessageListener and MessagingMessageListenerAdapter classes, to avoid unnecessary nesting when handling existing instances of the Message class and message conversion. More details on this release may be found in the release notes.
Spring for Apache Kafka
The first release candidate of Spring for Apache Kafka 4.2.0 provides bug fixes, documentation improvements, dependency upgrades and one new feature that now writes out the value defined in the KafkaHeaders.DELIVERY_ATTEMPT header when using the CommonDelegatingErrorHandler class in conjunction with the deliveryAttemptHeader container property set to true. Further details on this release may be found in the release notes.
Spring LDAP
The first release candidate of Spring LDAP 4.2.0 delivers bug fixes, dependency upgrades and new features such as: use of string parameterization in logging to avoid non-constant filename lengths; the addition of test cases for the DefaultObjectDirectoryMapperTests class; and string cleanup in the getStringAttribute() method, defined in DirContextAdapter class, to prevent a ClassCastException. More details on this release, including breaking changes, may be found in the release notes and what's new page.
Spring Web Services
The first release candidate of Spring Web Services 5.1.0 ships with documentation improvements dependency upgrades and one new feature that allows an instance of the DefaultWsdl11Definition class to attach a policy document, such as a WS-Policy or WS-SecurityPolicy fragment, to every binding it generates. Further details on this release may be found in the release notes and this wiki page.
