# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------

from ._index import (
    ComplexField,
    SearchField,
    SearchableField,
    SimpleField,
    SearchIndex,
)
from . import _edm as SearchFieldDataType
from ..._generated.models import SuggestOptions
from .._generated.models import (
    AnalyzeResult,
    AnalyzedTokenInfo,
    AsciiFoldingTokenFilter,
    BM25Similarity as BM25SimilarityAlgorithm,
    CharFilter,
    CjkBigramTokenFilter,
    ClassicSimilarity as ClassicSimilarityAlgorithm,
    ClassicTokenizer,
    CommonGramTokenFilter,
    ConditionalSkill,
    CorsOptions,
    DictionaryDecompounderTokenFilter,
    DistanceScoringFunction,
    DistanceScoringParameters,
    EdgeNGramTokenFilter,
    EdgeNGramTokenizer,
    EdgeNGramTokenFilterSide,
    ElisionTokenFilter,
    EntityCategory,
    EntityRecognitionSkill,
    EntityRecognitionSkillLanguage,
    FieldMapping,
    FieldMappingFunction,
    FreshnessScoringFunction,
    FreshnessScoringParameters,
    GetIndexStatisticsResult,
    ImageAnalysisSkill,
    ImageAnalysisSkillLanguage,
    ImageDetail,
    IndexingSchedule,
    IndexingParameters,
    IndexerExecutionStatus,
    IndexerStatus,
    InputFieldMappingEntry,
    KeepTokenFilter,
    KeyPhraseExtractionSkill,
    KeyPhraseExtractionSkillLanguage,
    KeywordMarkerTokenFilter,
    KeywordTokenizerV2 as KeywordTokenizer,
    LanguageDetectionSkill,
    LengthTokenFilter,
    LexicalAnalyzer,
    LexicalTokenizer,
    LimitTokenFilter,
    LuceneStandardAnalyzer,
    LuceneStandardTokenizer,
    MagnitudeScoringFunction,
    MagnitudeScoringParameters,
    MappingCharFilter,
    MergeSkill,
    MicrosoftLanguageStemmingTokenizer,
    MicrosoftLanguageTokenizer,
    MicrosoftStemmingTokenizerLanguage,
    MicrosoftTokenizerLanguage,
    NGramTokenFilter,
    NGramTokenizer,
    OcrSkill,
    OcrSkillLanguage,
    OutputFieldMappingEntry,
    PathHierarchyTokenizerV2 as PathHierarchyTokenizer,
    PatternCaptureTokenFilter,
    PatternReplaceCharFilter,
    PatternReplaceTokenFilter,
    PhoneticEncoder,
    PhoneticTokenFilter,
    RegexFlags,
    SearchIndexer,
    SearchIndexerDataContainer,
    SearchIndexerDataSourceType,
    SearchIndexerError,
    SearchIndexerLimits,
    SearchIndexerSkillset,
    SearchIndexerStatus,
    ScoringFunction,
    ScoringFunctionAggregation,
    ScoringFunctionInterpolation,
    ScoringProfile,
    SentimentSkill,
    SentimentSkillLanguage,
    ShaperSkill,
    ShingleTokenFilter,
    Similarity as SimilarityAlgorithm,
    SnowballTokenFilter,
    SnowballTokenFilterLanguage,
    SoftDeleteColumnDeletionDetectionPolicy,
    SplitSkill,
    SplitSkillLanguage,
    SqlIntegratedChangeTrackingPolicy,
    StemmerOverrideTokenFilter,
    StemmerTokenFilter,
    StemmerTokenFilterLanguage,
    StopAnalyzer,
    StopwordsList,
    StopwordsTokenFilter,
    Suggester as SearchSuggester,
    SynonymTokenFilter,
    TagScoringFunction,
    TagScoringParameters,
    TextSplitMode,
    TextTranslationSkill,
    TextTranslationSkillLanguage,
    TextWeights,
    TokenCharacterKind,
    TokenFilter,
    TokenFilterName,
    TruncateTokenFilter,
    UaxUrlEmailTokenizer,
    UniqueTokenFilter,
    WebApiSkill,
    VisualFeature,
    WordDelimiterTokenFilter,
)
from ._models import (
    AnalyzeTextOptions,
    CustomAnalyzer,
    PatternAnalyzer,
    PatternTokenizer,
    SearchIndexerDataSourceConnection,
    SearchResourceEncryptionKey,
    SynonymMap,
)


__all__ = (
    "AnalyzeTextOptions",
    "AnalyzeResult",
    "AnalyzedTokenInfo",
    "AsciiFoldingTokenFilter",
    "BM25SimilarityAlgorithm",
    "CharFilter",
    "CjkBigramTokenFilter",
    "ClassicSimilarityAlgorithm",
    "ClassicTokenizer",
    "CommonGramTokenFilter",
    "ComplexField",
    "ConditionalSkill",
    "CorsOptions",
    "CustomAnalyzer",
    "DictionaryDecompounderTokenFilter",
    "DistanceScoringFunction",
    "DistanceScoringParameters",
    "EdgeNGramTokenFilter",
    "EdgeNGramTokenizer",
    "ElisionTokenFilter",
    "EdgeNGramTokenFilterSide",
    "EntityCategory",
    "EntityRecognitionSkill",
    "EntityRecognitionSkillLanguage",
    "FieldMapping",
    "FieldMappingFunction",
    "FreshnessScoringFunction",
    "FreshnessScoringParameters",
    "GetIndexStatisticsResult",
    "ImageAnalysisSkill",
    "ImageAnalysisSkillLanguage",
    "ImageDetail",
    "IndexingSchedule",
    "IndexingParameters",
    "IndexerExecutionStatus",
    "IndexerStatus",
    "InputFieldMappingEntry",
    "KeepTokenFilter",
    "KeyPhraseExtractionSkill",
    "KeyPhraseExtractionSkillLanguage",
    "KeywordMarkerTokenFilter",
    "KeywordTokenizer",
    "LanguageDetectionSkill",
    "LengthTokenFilter",
    "LexicalAnalyzer",
    "LexicalTokenizer",
    "LimitTokenFilter",
    "LuceneStandardAnalyzer",
    "LuceneStandardTokenizer",
    "MagnitudeScoringFunction",
    "MagnitudeScoringParameters",
    "MappingCharFilter",
    "MergeSkill",
    "MicrosoftLanguageStemmingTokenizer",
    "MicrosoftLanguageTokenizer",
    "MicrosoftStemmingTokenizerLanguage",
    "MicrosoftTokenizerLanguage",
    "NGramTokenFilter",
    "NGramTokenizer",
    "OcrSkill",
    "OcrSkillLanguage",
    "OutputFieldMappingEntry",
    "PathHierarchyTokenizer",
    "PatternAnalyzer",
    "PatternCaptureTokenFilter",
    "PatternReplaceCharFilter",
    "PatternReplaceTokenFilter",
    "PatternTokenizer",
    "PhoneticEncoder",
    "PhoneticTokenFilter",
    "RegexFlags",
    "ScoringFunction",
    "ScoringFunctionAggregation",
    "ScoringFunctionInterpolation",
    "ScoringProfile",
    "SearchField",
    "SearchIndex",
    "SearchIndexer",
    "SearchIndexerDataContainer",
    "SearchIndexerDataSourceConnection",
    "SearchIndexerDataSourceType",
    "SearchIndexerError",
    "SearchIndexerLimits",
    "SearchIndexerSkillset",
    "SearchIndexerStatus",
    "SearchResourceEncryptionKey",
    "SearchableField",
    "SentimentSkill",
    "SentimentSkillLanguage",
    "ShaperSkill",
    "ShingleTokenFilter",
    "SimpleField",
    "SimilarityAlgorithm",
    "SnowballTokenFilter",
    "SnowballTokenFilterLanguage",
    "SoftDeleteColumnDeletionDetectionPolicy",
    "SplitSkill",
    "SplitSkillLanguage",
    "SqlIntegratedChangeTrackingPolicy",
    "StemmerOverrideTokenFilter",
    "StemmerTokenFilter",
    "StemmerTokenFilterLanguage",
    "StopAnalyzer",
    "StopwordsList",
    "StopwordsTokenFilter",
    "SearchSuggester",
    "SuggestOptions",
    "SynonymMap",
    "SynonymTokenFilter",
    "TagScoringFunction",
    "TagScoringParameters",
    "TextSplitMode",
    "TextTranslationSkill",
    "TextTranslationSkillLanguage",
    "TextWeights",
    "TokenCharacterKind",
    "TokenFilter",
    "TokenFilterName",
    "TruncateTokenFilter",
    "UaxUrlEmailTokenizer",
    "UniqueTokenFilter",
    "VisualFeature",
    "WebApiSkill",
    "WordDelimiterTokenFilter",
    "SearchFieldDataType",
)
