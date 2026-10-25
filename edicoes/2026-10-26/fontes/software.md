# PingCAP Breach Exposes Customer Records and Source Code

- Editoria: Software (`software`)
- Fonte: InfoQ — https://www.infoq.com/news/2026/10/pingcap-cloud-data-breach/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
- Autor: Renato Losio
- Publicado: 2026-10-25T06:27:00+00:00
- Score: 4.514
- Imagem: imagens/software-pingcap-breach-exposes-customer-records.jpg | crédito: InfoQ | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- nenhuma

## Texto extraído

PingCAP recently confirmed unauthorized access to its internal systems and the theft of source code and customer-related data. The attacker, cyber extortion group FulcrumSec, claimed to have stolen 10.6 TB of data, including TiDB Cloud control-plane records, customer SQL statements, API keys, connection logs, billing information, internal documents, and 413 private source-code repositories. These claims have not been independently verified.
FulcrumSec alleges that access continued undetected for many weeks and that some exposed credentials could provide access to customer systems. They write:
We possess the complete TiDB Cloud control plane, its billing and finance estate, its GCP storage estate and its AWS cost and billing estate, its Jira, its CRM, its analytics, its source code, and a four-year log of every connection every customer ever made to its product, from the IP addresses of their application servers.
PingCAP is the company behind TiDB, the open-source distributed SQL database compatible with MySQL. Its incident report states:
An external incident response firm reviewed PingCAP’s production systems and found no evidence that the attacker ran commands or maintained persistent access in the systems reviewed. That finding does not change the data exposure described below. With support from outside counsel and third-party forensic specialists, there is no evidence that data stored in TiDB was impacted.
PingCAP also confirmed that exported records included user names and email addresses, organization and project associations, and SQL editor text and errors, with some records also containing organization, project, and cluster identifiers.
The attacker claims to have obtained a complete copy of metadb, containing around 180K tenant organisations, almost 300K user records, including 166K real names, and over 400K unique email addresses. The data allegedly includes 115K console API keypairs, of which over 40K were active and the newest reportedly created hours before the attacker claims to have ended access. The group also says it obtained around 1800 external database endpoints from customer migration jobs, including root and admin accounts for customer MySQL and Aurora hosts.
FulcrumSec alleges that PingCAP engineers paste customers’ production credentials into Jira tickets, with three logs reproduced in full and the corresponding tickets included in the initial release. Kim Barthel, director and founder of 42Sec, warns:
The PingCAP breach isn't really a database story. It's a story about one service-account key (...) PingCAP says it has no evidence that customer data stored in TiDB itself was touched. Good. But look at what did leak. Whoever has it knows who your engineers are, what you pay, when your contract renews, and what your schema looks like. That's everything needed for a phishing email you'd actually believe.
The breach highlights how cloud providers can inadvertently store sensitive customer data in query histories, support tickets, and diagnostic logs, leaving customers exposed even when their own databases remain uncompromised. In the article covering recommended customer actions, PingCAP recommends that customers replace active TiDB Cloud management API keys and remain alert to targeted phishing attempts.
In a popular Hacker News thread, practitioners question PingCAP's response, with some highlighting the attacker's allegation that it repeatedly exported the control-plane database without triggering detection for over a month. User dherls writes:
If true, this is next level incompetence from PingCap. Apparently the attackers set up a replication pipeline for a month?!
Referring to the recent press release "TiDB Opens Source Code to Independent Security Review, Strengthens Enterprise Trust Program," user xKingfisher notes:
Coming this close on the heels of the security audit by NCC is pretty embarrassing for all parties.
The allegedly exposed records reportedly include data associated with companies such as Booking.com, Shopee, Airbnb, Pinterest, Databricks, Atlassian, Fujitsu, SoftBank, and Baidu, but this does not confirm that these organizations were compromised. For example, Bitget, one of the cryptocurrency exchanges mentioned in the report, said its investigation found no evidence that user data had been exposed.
FulcrumSec's first release consists of five tar.gz archives totalling 128.3 GB compressed and just over 200 GB uncompressed, out of a claimed 10.6 TB of data.
