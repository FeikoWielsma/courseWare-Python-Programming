export default {
  title: 'Python Programming',
  accent: '#24669a',
  // Explicit layout choices. Source slide boundaries are never changed.
  compactSlides: [
    '02-variables-and-data-types-7',
    '02-variables-and-data-types-11',
    '02-variables-and-data-types-13',
    '02-variables-and-data-types-23',
    '03-data-structures-3',
    '05-functions-3',
    '05-functions-5',
    '05-functions-12',
    '05-functions-13',
    '08-exception-handling-1',
    '08-exception-handling-16',
    '10-python-database-access-4',
    '10-python-database-access-5',
    '10-python-database-access-6',
    '11-python-classes-9',
    '13-appendix-libraries-1',
  ],
  enrichments: [
    { module: '03-data-structures', after: 'Accessing Lists', file: 'src/slidev/list-mutation.md' },
    { module: '03-data-structures', after: 'Usage of Tuples', file: 'src/slidev/tuple-unpacking.md' },
  ],
};
